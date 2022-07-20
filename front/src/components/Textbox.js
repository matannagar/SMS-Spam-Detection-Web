import React from 'react'

function Textbox({ query, setQuery }) {
    return (
        <div className="input-message">
            <div className="container">
                <input type="text"
                    placeholder="Insert message here..."
                    onChange={e => setQuery(e.target.value)}
                    value={query}
                />
            </div>
        </div>
    )
}

export default Textbox
