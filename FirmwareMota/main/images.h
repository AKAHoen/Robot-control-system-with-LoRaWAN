#define SATELLITE_IMAGE_WIDTH 16
#define SATELLITE_IMAGE_HEIGHT 15
const uint8_t SATELLITE_IMAGE[] PROGMEM = {
    0x00, 0x08, 0x00, 0x1C, 0x00, 0x0E, 0x20, 0x07, 0x70, 0x02, 0xF8, 0x00,
    0xF0, 0x01, 0xE0, 0x03, 0xC8, 0x01, 0x9C, 0x54, 0x0E, 0x52, 0x07, 0x48,
    0x02, 0x26, 0x00, 0x10, 0x00, 0x0E
};

#define TTN_IMAGE_WIDTH 62
#define TTN_IMAGE_HEIGHT 48
const uint8_t TTN_IMAGE[] PROGMEM = {
    0x00, 0x00, 0x00, 0xC0, 0x07, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xF0,
    0x3F, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xFC, 0x7F, 0x00, 0x70, 0x00,
    0x00, 0x00, 0x00, 0xFC, 0xFF, 0x00, 0xF0, 0x00, 0x00, 0x00, 0x00, 0xFF,
    0xFF, 0x01, 0xC0, 0x03, 0x00, 0x80, 0x1F, 0xFF, 0xFF, 0x03, 0x00, 0x07,
    0x00, 0xE0, 0xBF, 0xFF, 0xFF, 0x03, 0x38, 0x0E, 0x00, 0xF0, 0xFF, 0xFF,
    0xFF, 0x07, 0xF8, 0x0C, 0x00, 0xF0, 0xFF, 0xFF, 0xFF, 0xF7, 0xE3, 0x1C,
    0x00, 0xF0, 0xFF, 0xFF, 0xFF, 0xFF, 0xC7, 0x1D, 0x00, 0xFC, 0xFF, 0xFF,
    0xFF, 0xFF, 0x8F, 0x19, 0x00, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0x9F, 0x19,
    0x80, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0x9F, 0x19, 0xC0, 0xFF, 0xFF, 0xFF,
    0xFF, 0xFF, 0xBF, 0x19, 0xC0, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xBF, 0x19,
    0xC0, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0x3F, 0x18, 0xF8, 0xFF, 0xFF, 0xFF,
    0xFF, 0xFF, 0x3F, 0x00, 0xFC, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F, 0x00,
    0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F, 0x00, 0xFE, 0xFF, 0xFF, 0xFF,
    0xFF, 0xFF, 0x7F, 0x00, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0x7F, 0x00,
    0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0x00, 0xFF, 0xFF, 0xFF, 0xFF,
    0xFF, 0xFF, 0xFF, 0x00, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0x00,
    0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0x00, 0xFE, 0xFF, 0xFF, 0xFF,
    0xFF, 0xFF, 0x7F, 0x00, 0xFC, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0x7F, 0x00,
    0xF8, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F, 0x00, 0xE0, 0xFF, 0xFF, 0xFF,
    0xFF, 0xFF, 0x07, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0xBF, 0x99, 0xC7, 0x6F, 0x36, 0x63, 0x1C, 0x1C,
    0xBF, 0x99, 0xC7, 0x6F, 0x36, 0x67, 0x7E, 0x1E, 0x8C, 0x99, 0x00, 0x63,
    0x36, 0x67, 0x03, 0x02, 0x8C, 0x99, 0x00, 0x63, 0x36, 0x6F, 0x03, 0x06,
    0x8C, 0x9F, 0x07, 0xE3, 0x37, 0x6B, 0x73, 0x1C, 0x8C, 0x99, 0x00, 0x63,
    0x36, 0x7B, 0x63, 0x30, 0x8C, 0x99, 0x00, 0x63, 0x36, 0x73, 0x76, 0x33,
    0x8C, 0x99, 0x07, 0x63, 0x36, 0x73, 0x3E, 0x1F, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x08, 0x0C, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x12, 0x18, 0x3C, 0x28,
    0x81, 0x03, 0x07, 0x1A, 0x16, 0x08, 0x18, 0x68, 0x41, 0x06, 0x05, 0x0E,
    0x1E, 0x18, 0x18, 0x68, 0x41, 0x06, 0x07, 0x06, 0x1A, 0x08, 0x18, 0xD0,
    0x40, 0x06, 0x05, 0x0A, 0x12, 0x18, 0x18, 0xD0, 0x80, 0x01, 0x0D, 0x12,
};