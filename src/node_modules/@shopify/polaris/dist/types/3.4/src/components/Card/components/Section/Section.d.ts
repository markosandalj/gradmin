import React from 'react';
import { ComplexAction } from '../../../../types';
export interface CardSectionProps {
    title?: React.ReactNode;
    children?: React.ReactNode;
    subdued?: boolean;
    flush?: boolean;
    fullWidth?: boolean;
    /** Allow the card to be hidden when printing */
    hideOnPrint?: boolean;
    actions?: ComplexAction[];
}
export declare function Section({ children, title, subdued, flush, fullWidth, actions, hideOnPrint, }: CardSectionProps): JSX.Element;
