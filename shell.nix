with import <nixpkgs> {};
with pkgs.coreutils;
with pkgs.glibcLocales;
with pkgs.python36Packages;

buildPythonPackage rec {
  name = "chapterize";
  src = ".";
  propagatedBuildInputs = [ click ];
}
