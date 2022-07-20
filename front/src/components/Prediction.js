import React from 'react'

function Result({ result }) {
    return (
        <div className="prediction">
            <div className="container">
                <h2>{result}</h2>
            </div>
        </div>
    )
}

export default Result
