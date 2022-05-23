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
                            url: '/index/matura/5/list',
                            disabled: false,
                            label: 'Fizika',
                        },
                        {
                            url: '/index/matura/2/list',
                            disabled: false,
                            label: 'Matematika A',
                        },
                        {
                            url: '/index/matura/4/list',
                            disabled: false,
                            label: 'Matematika B',
                        },
                        {
                            url: '/index/matura/7/list',
                            disabled: true,
                            label: 'Kemija',
                        },
                        {
                            url: '/index/matura/6/list',
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
                        url: '/index/skripta/9/list',
                        disabled: false,
                        label: 'Matematika A',
                    },
                    {
                        url: '/index/skripta/8/list',
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
                {
                    url: '/index/problems_importer',
                    label: 'Problems importer',
                },
                {
                    url: '/index/cheatsheets/list',
                    label: 'Cheatsheets',
                }
                ]}
            />
        </Navigation>
    )
}

export default Sidebar;