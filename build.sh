#!/bin/bash
# SLF.Mine Build Script

VERSION=$1
if [ -z "$VERSION" ]; then
  echo "Usage: ./build.sh <version>"
  echo "Example: ./build.sh v1.0.0"
  exit 1
fi

# Ensure build directory exists
mkdir -p build

echo "Building Datapack ($VERSION)..."
cd data_pack
7z a -tzip "../build/SLFMine-Datapack-$VERSION.zip" . -xr!.* -xr!__MACOSX
cd ..

echo "Building Resource Pack ($VERSION)..."
cd resource_pack
7z a -tzip "../build/SLFMine-ResourcePack-$VERSION.zip" . -xr!.* -xr!__MACOSX
cd ..

echo "------------------------------------------------"
echo "Build complete! Files are in the build/ directory:"
ls -lh build/SLFMine-*-$VERSION.zip
