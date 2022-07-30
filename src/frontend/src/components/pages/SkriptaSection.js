import React from 'react'

// COMPONENTS
import { Problem } from '../parts/Problem';

// SHOPIFY
import { Card } from '@shopify/polaris';
import { EquationsTable } from '../EquationsTable';

export const SkriptaSection = ({ section, sectionNumber }) => {
    
    if(!section) return <></>;

    return (
        <Card title={`${sectionNumber}. ${section.name}`}>
            <Card.Section>
                <EquationsTable equations={section.equations} />
            </Card.Section>
            {section.problems?.map((problem) => {
                return (
                    <Card.Section key={problem.id}>
                        <Problem key={problem.id} problem={problem} />
                    </Card.Section>
                )
            })}
        </Card>
    )
}


//     <form id="printThis" onSubmit={handleSubmit} className={`skripta-${skripta_id}`}>
//             <button type="submit" className="btn btn--save">Save</button>
//             <button type="button" onClick={handlePrint} className="btn btn--primary">
//                 { downloadLoading ?
//                     <Oval    
//                         heigth="16"
//                         width="16"
//                         color='grey'
//                         ariaLabel='loading'>
//                     </Oval> : 'Print'}
//             </button>
//             {displayDownloadModal &&
//                 <div className="problems-section__modal">
//                     <h3>Skripta je spremna za preuzimanje</h3>
//                     <a className="btn btn--primary" href={downloadLink} target="_blank">Preuzmi</a>
//                 </div>
//             }
//         </div>