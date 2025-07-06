import { useWallet } from "@solana/wallet-adapter-react";
import { authenticateWallet } from "../api/walletApi";
import { useState } from "react";

export function useWalletAuth() {
  const { publicKey, signMessage } = useWallet();
  const [error, setError] = useState<string | null>(null);

  const authenticate = async () => {
    if (!publicKey || !signMessage) {
      setError("Wallet not connected or signMessage unavailable");
      return;
    }
    try {
      const message = "Authenticate with Solana Wallet";
      const encodedMessage = new TextEncoder().encode(message);
      const signature = await signMessage(encodedMessage);
      await authenticateWallet(publicKey.toBase58(), Buffer.from(signature).toString("base64"));
      setError(null);
    } catch (e: any) {
      setError(e.message);
    }
  };

  return { authenticate, error };
}
