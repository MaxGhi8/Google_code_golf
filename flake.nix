{
  description = "Simple flake for simple environment for google golf code";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs?ref=nixos-unstable";
  };

  outputs = { self, nixpkgs }:
    let pkgs = nixpkgs.legacyPackages.x86_64-linux;
    in {
      devShell.x86_64-linux =
        pkgs.mkShell {
          buildInputs = [
            pkgs.cowsay
            pkgs.neovim
            pkgs.python313
            pkgs.python313Packages.matplotlib
            pkgs.python313Packages.numpy
          ];
        };
    };
}
