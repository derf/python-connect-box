"""Handle Data attributes."""
from ipaddress import IPv4Address, IPv6Address, ip_address as convert_ip
from typing import List, Union

import attr

@attr.s
class Device:
    """A single device."""

    mac: str = attr.ib()
    hostname: str = attr.ib(cmp=False)
    ip: Union[IPv4Address, IPv6Address] = attr.ib(cmp=False, converter=convert_ip)

@attr.s
class CMState:
    """Modem state."""

    tunerTemperature: int = attr.ib()
    temperature: int = attr.ib()
    operState: str = attr.ib()
    ipv4Addresses: List[IPv4Address] = attr.ib(converter=lambda x: list(map(convert_ip, x)))
    ipv6Addresses: List[IPv6Address] = attr.ib(converter=lambda x: list(map(convert_ip, x)))

@attr.s
class DownstreamChannel:
    """A locked downstream channel."""

    frequency: int = attr.ib()
    powerLevel: int = attr.ib()
    modulation: str = attr.ib()
    id: str = attr.ib()
    snr: float = attr.ib()
    preRs: int = attr.ib()
    postRs: int = attr.ib()
    qamLocked: bool = attr.ib()
    fecLocked: bool = attr.ib()
    mpegLocked: bool = attr.ib()


@attr.s
class UpstreamChannel:
    """A locked upstream channel."""

    frequency: int = attr.ib()
    powerLevel: int = attr.ib()
    symbolRate: str = attr.ib()
    id: str = attr.ib()
    modulation: str = attr.ib()
    type: str = attr.ib()
    t1Timeouts: int = attr.ib()
    t2Timeouts: int = attr.ib()
    t3Timeouts: int = attr.ib()
    t4Timeouts: int = attr.ib()
    channelType: str = attr.ib()
    messageType: int = attr.ib()
