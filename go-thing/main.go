package main

import (
	"log"
	"os"
)

// import (
// "fmt"
// "strconv"
// "encoding/csv"
// "io"
// "os"
// )

func main() {
	quizFicle, fileOpenErr := os.Open("problems.csv")
	if (fileOpenErr != nil) {
		log.Fatal(fileOpenErr)
	}
}