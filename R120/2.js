function trackChanges() {
  const pastVersions = [];
  let now = -1;
  let browsingHistory = false;

  const stayInBounds = (position) => {
    if (position < 0) return 0;
    if (position >= pastVersions.length) return pastVersions.length - 1;
    return position;
  };

  return {
    save(...newStates) {
      if (browsingHistory) {
        pastVersions.splice(now + 1);
        browsingHistory = false;
      }
      pastVersions.push(...newStates);
      now = pastVersions.length - 1;
    },

    back(steps = 1) {
      now = stayInBounds(now - steps);
      browsingHistory = true;
      return pastVersions[now];
    },

    forward(steps = 1) {
      now = stayInBounds(now + steps);
      browsingHistory = now < pastVersions.length - 1;
      return pastVersions[now];
    },

    current() {
      return pastVersions[now];
    },

    history() {
      return [...pastVersions];
    },
  };
}
