// REACT & REDUX
import React from "react";
import { useSelector } from "react-redux";

// SHOPIFY
import { ButtonGroup, Button, Stack, VideoThumbnail } from "@shopify/polaris";

// QRcode
import QRCode from "qrcode.react";

// COMPONENTS
import  { Question } from "./Question";

// SETTINGS
import { REVIEW_VIEW_TYPE } from "../../settings/constants";

export const Problem = ({ problem }) => {
  	const viewType = useSelector(state => state.view.viewType);

	const playVideo = () => {
		return (
			<div className="problem__video">
				<iframe
					src={vimeo_embed_src}
					frameBorder="0"
					allow="autoplay; fullscreen; picture-in-picture"
					allowFullScreen
					title="26"
				/>
				<script src="https://player.vimeo.com/api/player.js" />
			</div>
		);
	};

	const isApproved = (approval) => approval === 'approved'

  	const Video =
		viewType === REVIEW_VIEW_TYPE
			? <VideoThumbnail
					videoLength={problem.video_solution?.length}
					thumbnailUrl={problem.video_solution?.vimeo_thumbnail_url || ''}
					onClick={playVideo}
				/>
			: null;

	const ApprovalButtons = 
		viewType === REVIEW_VIEW_TYPE ? 
			<div style={{ display: 'flex', justifyContent: "flex-end"}}>
				<ButtonGroup>
					<Button 
						destructive 
						disabled={!isApproved(problem.approval)}
					>
						{isApproved(problem.approval) ? 'Unapprove' : 'Unapproved'}
					</Button>
					<Button disabled={isApproved(problem.approval)} primary={!isApproved(problem.approval)}>
						{ isApproved(problem.approval) ? 'Approved' : 'Approve' }
					</Button>
				</ButtonGroup>
			</div>
			: null

	if(!problem) return <></>;

  	return (
		<>
			{Video}
			<Stack wrap={false}>
				<Stack.Item fill>
					<Question question={problem.question} />
				</Stack.Item>
				<Stack.Item>
					<a className="problem__qr-link" href={`https://gradivo.hr/products/${problem.matura?.product.handle}?brZad=${problem.id}`}>
						<QRCode value={`https://gradivo.hr/products/${problem.matura?.product.handle}?brZad=${problem.id}`} renderAs="svg" />
					</a>
				</Stack.Item>
			</Stack>
			{ApprovalButtons}
		</>
	);
};
