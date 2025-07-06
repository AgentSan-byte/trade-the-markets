import React, { useMemo, useState } from "react";
import { useWallet, WalletProvider, ConnectionProvider } from "@solana/wallet-adapter-react";
import { PhantomWalletAdapter, SolflareWalletAdapter } from "@solana/wallet-adapter-wallets";
import { logEvent } from "../utils/logger";

const CustomWalletButton: React.FC = () => {
  const { publicKey, connected, connecting, disconnecting, connect, disconnect, select, wallets, wallet } = useWallet();
  const [showWallets, setShowWallets] = useState(false);

  const handleConnect = async () => {
    if (!wallet) {
      setShowWallets(true);
      logEvent("wallet_select_opened", {});
    } else if (!connected) {
      logEvent("wallet_connect_attempt", { wallet: wallet.adapter.name });
      await connect();
      logEvent("wallet_connected", { wallet: wallet.adapter.name, publicKey: publicKey?.toBase58() });
    } else {
      logEvent("wallet_disconnect_attempt", { wallet: wallet.adapter.name });
      await disconnect();
      logEvent("wallet_disconnected", { wallet: wallet.adapter.name });
    }
  };

  return (
    <div>
      <button
        onClick={handleConnect}
        disabled={connecting || disconnecting}
        style={{ marginRight: 8 }}
      >
        {connected ? `Disconnect (${publicKey?.toBase58().slice(0, 4)}...${publicKey?.toBase58().slice(-4)})` : wallet ? (connecting ? "Connecting..." : "Connect") : "Select Wallet"}
      </button>
      {showWallets && (
        <div style={{ border: "1px solid #ccc", padding: 8, background: "#fff", position: "absolute", zIndex: 10 }}>
          {wallets.map((w) => (
            <button
              key={w.adapter.name}
              onClick={() => {
                select(w.adapter.name);
                setShowWallets(false);
                logEvent("wallet_selected", { wallet: w.adapter.name });
              }}
              style={{ display: "block", width: "100%", margin: "4px 0" }}
            >
              {w.adapter.name}
            </button>
          ))}
          <button onClick={() => setShowWallets(false)} style={{ marginTop: 8 }}>Close</button>
        </div>
      )}
    </div>
  );
};

export const WalletConnect: React.FC = () => {
  const endpoint = useMemo(() => "https://api.mainnet-beta.solana.com", []);
  const wallets = useMemo(() => [new PhantomWalletAdapter(), new SolflareWalletAdapter()], []);

  return (
    <ConnectionProvider endpoint={endpoint}>
      <WalletProvider wallets={wallets} autoConnect>
        <CustomWalletButton />
      </WalletProvider>
    </ConnectionProvider>
  );
};
