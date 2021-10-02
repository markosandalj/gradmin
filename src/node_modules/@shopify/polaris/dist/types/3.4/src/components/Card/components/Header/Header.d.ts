import React from 'react';
import { DisableableAction } from '../../../../types';
export interface CardHeaderProps {
    title?: React.ReactNode;
    actions?: DisableableAction[];
    children?: React.ReactNode;
}
export declare function Header({ children, title, actions }: CardHeaderProps): JSX.Element;
