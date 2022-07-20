import React from 'react'

function Button({ classify }) {

    return (
        <div className="button-outer">
            <button
                className="button"
                onClick={classify}
            >Click Here!</button>
        </div>
    )
}

export default Button
