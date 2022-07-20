import React from 'react'

function Result({ result, color }) {
    return (
        <div className="prediction">
            <h2 style={{ color: color }}>{result}</h2>
        </div>
    )
}

export default Result
