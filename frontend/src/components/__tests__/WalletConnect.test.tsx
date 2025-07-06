import { render, screen } from "@testing-library/react";
import { WalletConnect } from "../WalletConnect";

test("renders wallet connect button", () => {
  render(<WalletConnect />);
  expect(screen.getByRole("button")).toBeInTheDocument();
});
