const token = "AQUIgja4qZrxH-sMek6ME-Y6Tz5EcrPAstzVy9vkL0GORsEOwVx-uew_6Ru_GLtCOY1Ejw7ardcL3TeJAYJWKbLAL28jDBjUCOIoV5M8i053FgGhOt3au3hqEKybTvMBs3yPzs4xyiDlcl4XMr7eIRqkYrHwVcbNQjsMP70k1Poqc0NWVNb2hrzA9PA2kU0j7-Ap5aE8tSemoX930dHGGfvbrSmpsnDNyQNl_t5Jl1IFhsNMSFfgZu6W-KT_R-0gIqvnQF_Hylrc_dA4AGIkuQo6ZFeLGRLkgN75dUs4aJAGkuhddjBlWqcKMr-Mek5eb6V4ZLXoD7qSwoNH-8uySJ4iOIddDA";

async function postToLinkedIn(text) {
  // 1. Teri Person ID nikalenge
  const me = await fetch("https://api.linkedin.com/v2/userinfo", {
    headers: { Authorization: `Bearer ${token}` }
  }).then(r=>r.json());
  
  const personUrn = `urn:li:person:${me.sub}`;

  // 2. Post karenge
  const res = await fetch("https://api.linkedin.com/rest/posts", {
    method: "POST",
    headers: {
      "Authorization": `Bearer ${token}`,
      "Content-Type": "application/json",
      "LinkedIn-Version": "202401",
      "X-Restli-Protocol-Version": "2.0.0"
    },
    body: JSON.stringify({
      author: personUrn,
      commentary: text,
      visibility: "PUBLIC",
      distribution: { feedDistribution: "MAIN_FEED" },
      lifecycleState: "PUBLISHED"
    })
  });
  
  console.log(await res.json());
}

postToLinkedIn("Testing Content OS 02 se first post ");