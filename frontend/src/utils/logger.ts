export function logEvent(event: string, details: Record<string, any>) {
  // Log to console for local audit
  console.log(`[AUDIT] ${event}`, details);
  // Send to backend for persistent audit logging
  fetch("http://localhost:8000/api/log", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ event, details }),
  }).catch((err) => {
    console.warn("Failed to send log to backend", err);
  });
}
