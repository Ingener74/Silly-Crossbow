#ifndef SILLY_CROSSBOW_H_
#define SILLY_CROSSBOW_H_

#include <string>
#include <vector>

std::string SillyCrossbow();

class CropTransparent {
public:
    CropTransparent();
    CropTransparent(int width, int height, const std::vector<char>& buffer);
    CropTransparent(int width, int height, void* data);
    virtual ~CropTransparent();

    int getCroppedHeight() const;
    int getCroppedWidth() const;
    int getCroppedOffsetX() const;
    int getCroppedOffsetY() const;

private:
    void cropTransparent(int width, int height, const std::vector<char>& buffer);

    int _croppedWidth = 0, _croppedHeight = 0, _croppedOffsetX = 0, _croppedOffsetY = 0;
};

#endif
