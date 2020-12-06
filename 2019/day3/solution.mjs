import { readFileSync } from 'fs';


function main() {
    let wires = readData();

    let point = findIntersectionClosestToOrigin(wires);
    console.log(point)

    let stepCount = findFirstIntersection(wires);
    console.log(stepCount)
}


function readData() {
    var lines;
    try {
        lines = readFileSync('data.txt').toString('utf8').split("\n");
    } catch (err) {
        console.error(err);
    }

    var wires = [];
    for (var line of lines) {
        wires.push(line.split(","));
    }
    return wires;
}


function findIntersectionClosestToOrigin(wires) {
    var coords1 = new Set(wireToCoordinates(wires[0]).map((point) => point.asString()));
    var coords2 = new Set(wireToCoordinates(wires[1]).map((point) => point.asString()));
    let intersection = new Set([...coords1].filter(x => coords2.has(x)));
    intersection.delete("0,0");
    
    let minDistance = 999999999999999999999999;
    let minPoint = new Point(0, 0);
    for (var coordString of intersection) {
        let point = new Point(coordString);
        let pDistance = point.manhattanDistanceFromOrigin();
        if (pDistance < minDistance) {
            minDistance = pDistance;
            minPoint = point;
        }
    }
    return minPoint;
}


class Point {
    constructor(x, y) {
        if (y === undefined) {
            let coords = x.split(",");
            this.x = parseInt(coords[0]);
            this.y = parseInt(coords[1]);
        }
        else {
            this.x = x;
            this.y = y;
        }
    }

    asString() {
        return `${this.x},${this.y}`;
    }

    manhattanDistanceFromOrigin() {
        return Math.abs(this.x) + Math.abs(this.y);
    }
}


function wireToCoordinates(wire) {
    var coordinates = [new Point(0, 0)];
    for (var instruction of wire) {
        var direction = instruction[0];
        var amount = parseInt(instruction.slice(1));

        var x_sign, y_sign;
        switch (direction) {
            case "L":
                x_sign = -1;
                y_sign = 0;
                break;
            case "R":
                x_sign = 1;
                y_sign = 0;
                break;
            case "D":
                x_sign = 0;
                y_sign = -1;
                break;
            case "U":
                x_sign = 0;
                y_sign = 1;
                break;
        }

        var lastPoint = coordinates.slice(-1)[0];
        let last_x = lastPoint.x;
        let last_y = lastPoint.y;
        for (var index = 0; index < amount; index++) {
            let next_x = last_x + x_sign;
            let next_y = last_y + y_sign;
            coordinates.push(new Point(next_x, next_y));
            last_x = next_x;
            last_y = next_y;
        }
    }

    return coordinates;
}


function findFirstIntersection(wires) {
    let coords1 = wireToCoordinates(wires[0])
    let coordsSet1 = new Set(coords1.map((point) => point.asString()));
    let coords2 = wireToCoordinates(wires[1])
    let coordsSet2 = new Set(coords2.map((point) => point.asString()));
    let intersections = new Set([...coordsSet1].filter(x => coordsSet2.has(x)));
    intersections.delete("0,0");

    let stepsByCoords1 = new Map();
    for (var stepCount = 0; stepCount < coords1.length; stepCount++) {
        let coordStr = coords1[stepCount].asString();
        if (intersections.has(coordStr) && !stepsByCoords1.has(coordStr)) {
            stepsByCoords1.set(coordStr, stepCount);
        }
    }

    let stepsByCoords2 = new Map();
    for (var stepCount = 0; stepCount < coords2.length; stepCount++) {
        let coordStr = coords2[stepCount].asString();
        if (intersections.has(coordStr) && !stepsByCoords2.has(coordStr)) {
            stepsByCoords2.set(coordStr, stepCount);
        }
    }

    let minSteps = 999999999999999999999999999;
    for (var coordStr of intersections) {
        let steps = stepsByCoords1.get(coordStr) + stepsByCoords2.get(coordStr);
        if (steps < minSteps) {
            minSteps = steps;
        }
    }

    return minSteps;
}


main();
