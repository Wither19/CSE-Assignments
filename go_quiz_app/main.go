package main

// https://github.com/gophercises/quiz

import (
	"encoding/csv"
	"fmt"
	"log"
	"os"
	"strconv"
)

func main() {
	quizFile, fileOpenErr := os.Open("problems.csv")
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

	convertedAnswer, conversionErr := strconv.ParseInt(answer, 0, 0)
	if (conversionErr != nil) {
		log.Fatal(conversionErr)
	} 

	convertedCorrectAnswer, correctAnswerConvErr := strconv.ParseInt(a, 0, 0)
	if (correctAnswerConvErr != nil) {
		log.Fatal(conversionErr)
	}

	if (convertedCorrectAnswer == convertedAnswer) {
		fmt.Println("\nCorrect!")
		isCorrect = 1

	} else {
		fmt.Println("\nIncorrect")
	}

	return isCorrect

}