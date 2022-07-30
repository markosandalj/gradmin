import React from 'react'
import { BrowserRouter } from 'react-router-dom'

// SETTINGS
import { logo } from './settings/logo'
import { userMenuActions } from './settings/userMenuActions'
import { sidebarItems } from './settings/sidebarItems'

// REDUX
import { useSelector, useDispatch } from 'react-redux'
import { closeToast } from './store/toastSlice'
import { closeSaveBar } from './store/saveBarSlice'
import { resetUpdateQueue } from './store/updateSlice'
import { toggleMobileNavigation, toggleUserMenu } from './store/pageSlice'

// SHOPIFY 
import { ContextualSaveBar, Toast, Frame, TopBar, Page, Modal, Navigation, Layout, SkeletonPage, Card, TextContainer, SkeletonBodyText, SkeletonDisplayText, AppProvider } from '@shopify/polaris'

// COMPONENTS
import RouteSwitcher from './components/RouteSwitcher'

export const App = () => {
    const dispatch = useDispatch()

    const isToastActive = useSelector(store => store.toast.isActive)
    const toastContent = useSelector(store => store.toast.content)
    const toastError = useSelector(store => store.toast.error)
    const toastDuration = useSelector(store => store.toast.duration)

    const isBannerActive = useSelector(store => store.banner.isOpen)
    const bannerStatus = useSelector(store => store.banner.status)
    const bannerTitle = useSelector(store => store.banner.title)
    const bannerMessage = useSelector(store => store.banner.message)

    const isSaveBarActive = useSelector(store => store.saveBar.isActive)
    const saveBarNessage = useSelector(store => store.saveBar.message)
    const saveBarApiUrl = useSelector(store => store.toast.apiUrl)

    const isModalOpen = useSelector(store => store.modal.isOpen)
    const modalTitle = useSelector(store => store.modal.title)

    const isPageLoading =  useSelector(store => store.toast.isLoading)
    const userMenuOpen = useSelector(store => store.toast.userMenuOpen)
    const pageTitle = useSelector(store => store.toast.pageTitle)
    const isMobileNavigationActive = useSelector(store => store.page.isMobileNavigationActive)

    const handleSaveChanges = () => {
        console.log('TODO: Save changed items')
    }

    const handleDiscardChanges = () => {
        dispatch(closeSaveBar())
        dispatch(resetUpdateQueue())
    }

    const toastMarkup = isToastActive ? (
        <Toast onDismiss={() => dispatch(closeToast())} content={toastContent} error={toastError} duration={toastDuration} />
      ) : null;

    const contextualSaveBarMarkup = isSaveBarActive ? (
        <ContextualSaveBar
            message={saveBarNessage}
            fullWidth
            saveAction={{
                content: 'Save',
                onAction: handleSaveChanges, // @todo: dodati neki useCallback ili obicnu funkciju sa post requestom
            }}
            discardAction={{
                content: 'Discard',
                onAction: handleDiscardChanges, // @todo: dunno, usless za sad
            }}
        />
      ) : null;

    const modalMarkup = isModalOpen ? (
        <Modal title={modalTitle}>
        </Modal>
    ) : null;

    const userMenuMarkup = (
        <TopBar.UserMenu
            actions={userMenuActions}
            name="Admin"
            detail={'Gradivo.hr admin'}
            initials="G"
            open={userMenuOpen}
            onToggle={() => dispatch(toggleUserMenu())}
        />
    );

    const topBarMarkup = (
        <TopBar
            showNavigationToggle
            userMenu={userMenuMarkup}
            onNavigationToggle={() => dispatch(toggleMobileNavigation())}
        />
    )

    const navigationMarkup = (
        <Navigation location="/">
            <Navigation.Section
                items={sidebarItems}
            />
        </Navigation>
    );

    const actualPageMarkup = (
        <Page title={pageTitle}>
          <Layout>
            <RouteSwitcher />
          </Layout>
        </Page>
    )

    const loadingPageMarkup = (
        <SkeletonPage>
            <Layout>
                <Layout.Section>
                    <Card sectioned>
                        <TextContainer>
                            <SkeletonDisplayText size="small" />
                            <SkeletonBodyText lines={9} />
                        </TextContainer>
                    </Card>
                </Layout.Section>
            </Layout>
        </SkeletonPage>
    );

    const loadingMarkup = isPageLoading ? <Loading /> : null;
    const pageMarkup = isPageLoading ? loadingPageMarkup : actualPageMarkup;

    return (
            <AppProvider
                i18n={{
                    Polaris: {
                        ResourceList: {
                            sortingLabel: "Sort by",
                            defaultItemSingular: "item",
                            defaultItemPlural: "items",
                            showing: "Showing {itemsCount} {resource}",
                            Item: {
                                viewItem: "View details for {itemName}",
                            },
                        },
                        Common: {
                            checkbox: "checkbox",
                        },
                    },
                }}
        >
            <BrowserRouter>
                <Frame
                    logo={logo}
                    topBar={topBarMarkup}
                    navigation={navigationMarkup}
                    showMobileNavigation={isMobileNavigationActive}
                    onNavigationDismiss={() => dispatch(toggleMobileNavigation())}
                >   
                    {contextualSaveBarMarkup}
                    {loadingMarkup}
                    {pageMarkup}
                    {toastMarkup}
                    {modalMarkup}
                </Frame>
            </BrowserRouter>
        </AppProvider>
    )
}

