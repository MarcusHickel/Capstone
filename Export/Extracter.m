file = '/home/marcus/rockettrackingplatform/GazeboExport/data1';
bag = ros2bagreader(file);

msgs = readMessages(bag);

for i = 1:length(msgs)

    if msgs{i,1}.name(1) == "azimuth_joint"
        table.azimuth.position(1,i) = msgs{i,1}.position(1);
        table.azimuth.velocity(1,i) = msgs{i,1}.velocity(1);

        table.altitude.position(1,i) = msgs{i,1}.position(2);
        table.altitude.velocity(1,i) = msgs{i,1}.velocity(2);
    else
        table.altitude.position(1,i) = msgs{i,1}.position(1);
        table.altitude.velocity(1,i) = msgs{i,1}.velocity(1);

        table.azimuth.position(1,i) = msgs{i,1}.position(2);
        table.azimuth.velocity(1,i) = msgs{i,1}.velocity(2);
    end

end

for i = 1:10000
    table.azimuth.position(i) = (floor(table.azimuth.position(i)/2*pi)-table.azimuth.position(i)/2*pi)*2*pi;
end