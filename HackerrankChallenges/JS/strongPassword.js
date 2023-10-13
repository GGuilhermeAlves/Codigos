function minimumNumber(n, password) {
    let missingTypes = 0;

    if (!password.match(/[0-9]/)) {
        missingTypes++;
    }
    if (!password.match(/[a-z]/)) {
        missingTypes++;
    }
    if (!password.match(/[A-Z]/)) {
        missingTypes++;
    }
    if (!password.match(/[!@#$%^&*()\-+]/)) {
        missingTypes++;
    }
    
    const minLength = 6;

    if (n < minLength) {
        return Math.max(missingTypes, minLength - n);
    } else {
        return missingTypes;
    }
}