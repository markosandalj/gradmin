import React, { Component, useState, useEffect } from "react";
import axios from 'axios'
import { useParams } from 'react-router';

import { Navigation, HomeMajor, ProductsMajor, OrdersMajor } from '@shopify/polaris';

const Sidebar = () => {
    
    return (
        <Navigation location="/">
            <Navigation.Section
                items={[
                {
                    url: '/index',
                    label: 'Home',
                },
                {
                    url: '/index/matura',
                    label: 'Mature',
                    selected: true,
                    subNavigationItems: [
                        {
                            url: '/index/matura/fizika',
                            disabled: false,
                            label: 'Fizika',
                        },
                        {
                            url: '/index/matura/matematika/a',
                            disabled: false,
                            label: 'Matematika A',
                        },
                        {
                            url: '/index/matura/matematika/b',
                            disabled: false,
                            label: 'Matematika B',
                        },
                        {
                            url: '/index/matura/kemija',
                            disabled: true,
                            label: 'Kemija',
                        },
                        {
                            url: '/index/matura/informatika',
                            disabled: true,
                            label: 'Informatika',
                        },
                    ],
                },
                {
                    url: '/index/skripta',
                    label: 'QR Skripta',
                    selected: true,
                    subNavigationItems: [
                    {
                        url: '/index/skripta/4/list',
                        disabled: false,
                        label: 'Fizika',
                    },
                    {
                        url: '/index/skripta/2/list',
                        disabled: false,
                        label: 'Matematika A',
                    },
                    {
                        url: '/index/skripta/3/list',
                        disabled: false,
                        label: 'Matematika B',
                    },
                    {
                        url: '/index/skripta/5/list',
                        disabled: true,
                        label: 'Kemija',
                    },
                    {
                        url: '/index/skripta/6/list',
                        disabled: true,
                        label: 'Informatika',
                    },
                    ],
                },
                ]}
            />
        </Navigation>
    )
}

export default Sidebar;