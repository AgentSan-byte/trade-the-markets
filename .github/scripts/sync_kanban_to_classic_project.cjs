// sync_kanban_to_classic_project.cjs
// Now loads environment variables from .env file if present
// Usage: Set MY_USERNAME, MY_TOKEN, and PROJECT_NUMBER env vars, then run with Node.js
// Syncs your Markdown Kanban board to a classic GitHub Project (personal account)
// - Adds missing cards to the correct columns
// - Does not remove or move existing cards (idempotent add only)

require('dotenv').config({ path: '.env' });

const fs = require('fs');
const fetch = require('node-fetch');

const USERNAME = process.env.MY_USERNAME;
const TOKEN = process.env.MY_TOKEN;
const PROJECT_NUMBER = process.env.PROJECT_NUMBER;
const BOARD_PATH = 'docs/gist_tracking_board.md';

if (!USERNAME || !TOKEN || !PROJECT_NUMBER) {
  console.error('Set MY_USERNAME, MY_TOKEN, and PROJECT_NUMBER env vars.');
  process.exit(1);
}

function parseKanban() {
  const content = fs.readFileSync(BOARD_PATH, 'utf8');
  const rows = content.split('\n').filter(line => line.startsWith('|'));
  const columns = rows[0].split('|').map(h => h.trim()).filter(Boolean);
  const items = { 'To Do': [], 'In Progress': [], 'Review': [], 'Done': [] };
  for (let i = 2; i < rows.length; i++) {
    const cells = rows[i].split('|').map(c => c.trim());
    for (let col = 1; col <= 4; col++) {
      if (cells[col]) {
        const match = cells[col].match(/\[(.+?)\]\((.+?)\)/);
        if (match) {
          items[columns[col - 1]].push({ title: match[1], url: match[2] });
        }
      }
    }
  }
  return items;
}

async function getProjectId() {
  const res = await fetch(`https://api.github.com/users/${USERNAME}/projects`, {
    headers: { 'Authorization': `token ${TOKEN}`, 'Accept': 'application/vnd.github.inertia-preview+json' }
  });
  const projects = await res.json();
  if (!Array.isArray(projects)) {
    console.error('GitHub API did not return a project list:', projects);
    process.exit(1);
  }
  const project = projects.find(p => p.number === parseInt(PROJECT_NUMBER));
  if (!project) {
    console.error('Project not found.');
    process.exit(1);
  }
  return project.id;
}

async function getColumns(projectId) {
  const res = await fetch(`https://api.github.com/projects/${projectId}/columns`, {
    headers: { 'Authorization': `token ${TOKEN}`, 'Accept': 'application/vnd.github.inertia-preview+json' }
  });
  return await res.json();
}

async function getCards(columnId) {
  const res = await fetch(`https://api.github.com/projects/columns/${columnId}/cards`, {
    headers: { 'Authorization': `token ${TOKEN}`, 'Accept': 'application/vnd.github.inertia-preview+json' }
  });
  return await res.json();
}

async function addCard(columnId, note) {
  await fetch(`https://api.github.com/projects/columns/${columnId}/cards`, {
    method: 'POST',
    headers: { 'Authorization': `token ${TOKEN}`, 'Accept': 'application/vnd.github.inertia-preview+json' },
    body: JSON.stringify({ note })
  });
}

async function main() {
  const kanban = parseKanban();
  const projectId = await getProjectId();
  const columns = await getColumns(projectId);
  for (const col of columns) {
    const colName = col.name.trim();
    if (!kanban[colName]) continue;
    const cards = await getCards(col.id);
    const cardNotes = cards.map(card => card.note && card.note.trim());
    for (const item of kanban[colName]) {
      const note = `${item.title} - ${item.url}`;
      if (!cardNotes.includes(note)) {
        await addCard(col.id, note);
        console.log(`Added card to ${colName}: ${note}`);
      }
    }
  }
}

main();
