const express = require("express");
const router = express.Router();
const invitationController = require("./invitationController");

router.post("/invitations", invitationController.createInvitation);
router.get("/invitations", invitationController.getInvitations);
router.put("/invitations/:id", invitationController.updateInvitation);
router.delete("/invitations/:id", invitationController.deleteInvitation);
router.patch("/invitations/:id/send", invitationController.sendInvitation);

module.exports = router;
