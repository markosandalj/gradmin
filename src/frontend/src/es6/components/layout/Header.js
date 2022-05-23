import React, { Component, useState, useEffect, useCallback } from "react";
import { Link } from "react-router-dom";

const Header = () => {
    const [userDropdownOpen, setUserDropdownOpen] = useState(false)
    const [userInitials, setUserInitals] = useState('M')
    const [userName, setUserName] = useState('User #123')

    const handleUserDropdown = () => {
        setUserDropdownOpen((userDropdownOpen) => !userDropdownOpen )
    }

    return (
        <header className="header">
            <div className="header__logo"></div>
            <div className="header__user" onClick={handleUserDropdown}>
                <div className="user__icon">{userInitials}</div>
                <div className="user__label">{userName}</div>
                <div className={ `user__dropdown ${ userDropdownOpen ?  'open' : ''}` }>
                    <div className="user__dropdown-item">Test</div>
                    <div className="user__dropdown-item">Test</div>
                    <div className="user__dropdown-item">Test</div>
                </div>
            </div>
        </header>
    )
}
export default Header;