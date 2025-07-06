export async function authenticateWallet(address: string, signature: string) {
  const response = await fetch("/api/wallet/auth", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ address, signature }),
  });
  if (!response.ok) throw new Error("Authentication failed");
  return response.json();
}
