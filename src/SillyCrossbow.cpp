#include "SillyCrossbow.h"

#include <iostream>

using namespace std;

std::string SillyCrossbow() {
    std::string desc = "Silly Crossbow is SWIG + distutils + crop transparent image borders example";
    cout << desc << endl;
    return desc;
}

CropTransparent::CropTransparent() {
}

CropTransparent::CropTransparent(int width, int height, const std::vector<char>& buffer) {
    cropTransparent(width, height, buffer);
}

CropTransparent::CropTransparent(int width, int height, void* data) {
    cropTransparent(width, height,
        vector<char> { static_cast<char*>(data), static_cast<char*>(data) + width * height * 4 });
}

CropTransparent::~CropTransparent() {
}

int CropTransparent::getCroppedWidth() const {
    return _croppedWidth;
}

int CropTransparent::getCroppedHeight() const {
    return _croppedHeight;
}

int CropTransparent::getCroppedOffsetX() const {
    return _croppedOffsetX;
}

int CropTransparent::getCroppedOffsetY() const {
    return _croppedOffsetY;
}

void CropTransparent::cropTransparent(int width, int height, const std::vector<char>& buffer) {
}
