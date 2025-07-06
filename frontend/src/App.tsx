import React from "react";
import { WalletConnect } from "./components/WalletConnect";

const App: React.FC = () => (
  <div style={{ padding: 32 }}>
    <h1>Solana Wallet App</h1>
    <WalletConnect />
  </div>
);

export default App;
