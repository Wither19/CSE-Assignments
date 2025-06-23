package main

// https://github.com/gophercises/quiz

import (
	"encoding/csv"
	"flag"
	"fmt"
	"log"
	"os"
)

func main() {

	problemFile := flag.String("file", "problems.csv", "Provide the location of the problems you'd like to quiz on, as a CSV.")

	flag.Parse()

	quizFile, fileOpenErr := os.Open(*problemFile)

	if (fileOpenErr != nil) {
		log.Fatal(fileOpenErr)
	} else {
		fmt.Println("Problems successfully loaded!")
	}

	reader := csv.NewReader(quizFile)

	problems, problemsErr := reader.ReadAll()

	if (problemsErr != nil) {
		log.Fatal(problemsErr)
	} 

	correctAnswerCount := 0

		for i, problem := range problems {
			correctAnswerCount += presentProblem(i, problem[0], problem[1])

			if (i == len(problems) - 1) {
				fmt.Printf("Your results:\n%d/%d answered correctly\n", correctAnswerCount, len(problems))
			}
		}
}

func presentProblem(n int, p string, a string) int {
	displayProblemNum := n + 1
	isCorrect := 0
	
	var answer string

	fmt.Printf("#%d. %v ", displayProblemNum, p)
	fmt.Scanln(&answer)

	if (answer == a) {
		fmt.Println("\nCorrect!")
		isCorrect = 1

	} else {
		fmt.Println("\nIncorrect")
	}

	return isCorrect

}