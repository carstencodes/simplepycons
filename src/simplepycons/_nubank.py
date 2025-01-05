#
# SPDX-License-Identifier: MIT
#
# Copyright (c) 2025 Carsten Igel.
#
# This file is part of simplepycons
# (see https://github.com/carstencodes/simplepycons).
#
# This file is published using the MIT license.
# Refer to LICENSE for more information
#
""""""
# pylint: disable=C0302
# Justification: Code is generated

from typing import TYPE_CHECKING

from .base_icon import Icon

if TYPE_CHECKING:
    from collections.abc import Iterable


class NubankIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "nubank"

    @property
    def original_file_name(self) -> "str":
        return "nubank.svg"

    @property
    def title(self) -> "str":
        return "Nubank"

    @property
    def primary_color(self) -> "str":
        return "#820AD1"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Nubank</title>
     <path d="M7.2795 5.4336c-1.1815 0-2.1846.4628-2.9432
 1.252h-.002c-.0541-.0022-.1074-.002-.162-.002-1.5436
 0-2.9925.8835-3.699 2.2559-.3088.5996-.4234 1.2442-.459
 1.9003-.0321.589 0 1.1863 0 1.7696v5.6523H3.184s.0022-2.784
 0-5.1777c-.0014-1.6112-.0118-3.0471 0-3.3418.056-1.3937.4372-2.3053
 1.1484-3.0508 2.3585.0018 3.8852 1.6091 3.9705 4.168.0196.5874.0254
 3.7304.0254
 3.7304v3.672h3.1678v-4.965c0-1.5007.0127-2.8006-.0918-3.6952-.292-2.5-1.821-4.168-4.1248-4.168zm8.3903.3008l-3.166.0039v4.9648c0
 1.5009-.0127 2.8007.0919 3.6953.2921 2.5001 1.821 4.168 4.1248 4.168
 1.1815 0 2.1846-.4628 2.9432-1.252.0003-.0003.0016.0004.002 0
 .0542.0023.1093.002.164.002 1.5435 0 2.9905-.8835
 3.6971-2.2558.3088-.5997.4233-1.2442.459-1.9004.032-.5889 0-1.1862
 0-1.7695V5.7383H20.816s-.0022 2.784 0 5.1777c.0015 1.6113.0119 3.047
 0 3.3418-.056 1.3935-.4372 2.3053-1.1483
 3.0508-2.3586-.0018-3.8853-1.6091-3.9706-4.168-.0196-.5874-.0273-2.0437-.0273-3.7324Z"
 />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return ''''''

    @property
    def license(self) -> "tuple[str | None, str | None]":
        _type: "str | None" = ''''''
        _url: "str | None" = ''''''

        if _type is not None and len(_type) == 0:
            _type = None

        if _url is not None and len(_url) == 0:
            _url = None

        return _type, _url

    @property
    def aliases(self) -> "Iterable[str]":
        yield from []
