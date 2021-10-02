import { useEffect, useLayoutEffect } from 'react';
import { isServer } from './target.js';

const useIsomorphicLayoutEffect = isServer ? useEffect : useLayoutEffect;

export { useIsomorphicLayoutEffect };
