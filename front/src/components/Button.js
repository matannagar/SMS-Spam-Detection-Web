import React from 'react'

function Button({ classify }) {
    return (
        <div className="button-outer">
            <div className="container">
                <button
                    className="button"
                    onClick={classify}
                >Click Here!</button>
            </div>
        </div>
    )
}

export default Button
