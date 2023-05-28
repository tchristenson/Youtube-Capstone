import React from 'react';
import styles from './Footer.module.css'

function Footer({ isLoaded }){

	return (
        <div className={styles['footer']}>
            <ul className={styles['container']}>
                <li className={styles['link']}>
                    <a href="https://github.com/tchristenson">Github</a>
                </li>
                <li className={styles['name']}>
                    Tommy Christenson
                </li>
                <li className={styles['link']}>
                <a href="https://www.linkedin.com/in/tommychristenson/">LinkedIn</a>
                </li>
            </ul>
        </div>
	);
}

export default Footer;
