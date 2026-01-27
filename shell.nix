{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  buildInputs = with pkgs; [
    python311
    python311Packages.pip
    python311Packages.virtualenv
    nodejs_20
    nodePackages.npm
    sqlite
  ];

  shellHook = ''
    echo "Ambiente chat_agno carregado!"
    echo "Python: $(python --version)"
    echo "Node.js: $(node --version)"
    
    # Setup venv se não existir
    if [ ! -d "backend/.venv" ]; then
      python -m venv backend/.venv
    fi
    source backend/.venv/bin/activate
  '';
}
