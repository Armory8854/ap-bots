{ pkgs ? import <nixpkgs> {} }:
  pkgs.mkShell {
    # nativeBuildInputs is usually what you want -- tools you need to run
    nativeBuildInputs = [ 
      pkgs.python310
      pkgs.python310Packages.feedparser
      pkgs.python310Packages.configparser
      pkgs.sqlite
    ];
}

