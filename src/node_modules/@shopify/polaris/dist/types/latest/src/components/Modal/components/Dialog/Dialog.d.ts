import React from 'react';
export interface DialogProps {
    labelledBy?: string;
    instant?: boolean;
    children?: React.ReactNode;
    limitHeight?: boolean;
    large?: boolean;
    small?: boolean;
    onClose(): void;
    onEntered?(): void;
    onExited?(): void;
    in?: boolean;
}
export declare function Dialog({ instant, labelledBy, children, onClose, onExited, onEntered, large, small, limitHeight, ...props }: DialogProps): JSX.Element;
