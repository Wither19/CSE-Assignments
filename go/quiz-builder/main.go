package main

import (
	"encoding/csv"
	"fmt"
	"log"
	"os"
	"strings"
)

func main() {
	newQuizFile, quizFileErr := os.Create("new_quiz.csv")
	if (quizFileErr != nil) {
		log.Fatal(quizFileErr)
	}
	
	quizWriter := csv.NewWriter(newQuizFile)

	questionAdding := true

	var question string
	var answer string

	for (questionAdding) {
		var addQuestion string
		var addAnother string
		fmt.Print("Question: ")
		fmt.Scanln(&question)

		fmt.Print("Answer: ")
		fmt.Scanln(&answer)
		fmt.Println()

		fmt.Printf("Q: %v\nA: %v\n\nWould you like to add this question? (y/n) ", question, answer)
		fmt.Scanln(&addQuestion)
		fmt.Println()

		if (strings.ToLower(addQuestion) == "y") {
			quizWriter.Write([]string{question, answer})
		}

		fmt.Printf("Would you like to add another question? (y/n) ")
		fmt.Scanln(&addAnother)
		fmt.Println()

		if (strings.ToLower(addAnother) == "n") {
			questionAdding = false
		}

		quizWriter.Flush()
		fmt.Printf("Questions successfully written to %v\n", newQuizFile.Name())
	} 
}