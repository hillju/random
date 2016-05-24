package main

import "os"
import "fmt"
import "image"
import "image/png"
import "net/http"

func fetchImage(url string) (image.Image) {
    resp, err := http.Get(url)
    if err != nil {
        fmt.Printf("ERROR: %v\n", err)
    }
    defer resp.Body.Close()

    img, _, err := image.Decode(resp.Body)
    if err != nil {
        fmt.Printf("Not a valid image file. Error: %v\n", err)
    }
    return img
}

func saveImage(name string, img image.Image) {
    file, _ := os.Create(name)
    defer file.Close()

    png.Encode(file, img)
}

func main() {
    testImageUrl := "https://upload.wikimedia.org/wikipedia/commons/c/c4/PM5544_with_non-PAL_signals.png"
    img := fetchImage(testImageUrl)
    saveImage("testImage.png", img)
}
