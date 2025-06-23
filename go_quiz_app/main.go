package main

// https://github.com/gophercises/quiz

import (
	"encoding/csv"
	"flag"
	"fmt"
	"log"
	"os"
	"strings"
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
			correctAnswerCount += presentProblem(i, problem)

			if (i == len(problems) - 1) {
				fmt.Printf("\nYour results:\n%d/%d answered correctly\n", correctAnswerCount, len(problems))
			}
		}
}

func presentProblem(questionNum int, problemSet []string) int {
	displayProblemNum := questionNum + 1
	isCorrect := 0

	problem := problemSet[0]
	answer := problemSet[1]
	
	var userAnswer string

	fmt.Printf("#%d. %v ", displayProblemNum, problem)
	fmt.Scanln(&userAnswer)

	userAnswer = strings.Trim(strings.ToLower(userAnswer), " ")

	if (userAnswer == answer) {
		fmt.Println("\nCorrect!")
		isCorrect = 1

	} else {
		fmt.Println("\nIncorrect")
	}

	return isCorrect

}