import React, { useState } from "react";

export default function ProblemSinglePrint(problem) {
    const [problemText, setProblemText] = useState(problem.problem.question.question_text)

    return (
        <div className="problem">
            <span>{problemText}</span>
        </div>
    )
}