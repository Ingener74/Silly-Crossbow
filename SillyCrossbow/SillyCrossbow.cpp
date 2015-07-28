#include "../SillyCrossbow/SillyCrossbow.h"

#include <iostream>

using namespace std;

std::string SillyCrossbow() {
    return "Silly Crossbow is SWIG + distutils + crop transparent image borders example";
}

CropTransparent::CropTransparent() {
}

CropTransparent::CropTransparent(int width, int height, int threshold, const std::vector<char>& buffer) {
    cropTransparent(width, height, threshold, buffer);
}

CropTransparent::CropTransparent(int width, int height, int threshold, const char* data) {
    cropTransparent(width, height, threshold, {data, data + width*height*4});
}

CropTransparent::CropTransparent(int width, int height, int threshold, void* data) {
    cropTransparent(width, height, threshold, {static_cast<char*>(data), static_cast<char*>(data) + width*height*4});
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

void CropTransparent::cropTransparent(int width, int height, int threshold, const std::vector<char>& buffer) {
}

