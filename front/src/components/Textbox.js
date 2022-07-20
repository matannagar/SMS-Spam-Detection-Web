import React from 'react'

function Textbox({ query, setQuery, setResult }) {
    return (
        <div className="input-message">
            <input type="text"
                placeholder="Insert message here..."
                onChange={e => setQuery(e.target.value)}
                value={query}
            />
        </div>
    )
}

export default Textbox
