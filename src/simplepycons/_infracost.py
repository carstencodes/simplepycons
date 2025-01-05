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


class InfracostIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "infracost"

    @property
    def original_file_name(self) -> "str":
        return "infracost.svg"

    @property
    def title(self) -> "str":
        return "Infracost"

    @property
    def primary_color(self) -> "str":
        return "#DB44B8"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Infracost</title>
     <path d="M15.5526 0.44419L8.04 7.98337H12.0699C14.7831 7.98337
 16.02 10.546 16.02 11.9876V23.3593C16.02 23.7131 16.3058 24 16.6584
 24H23.3217C23.6743 24 23.9601 23.7141 23.9606 23.3603C23.9652 20.0654
 24 13.2819 24 7.98337C24 3.34017 20.3118 0.33410 16.6801
 0.00515C16.2585 -0.03303 15.8518 0.14382 15.5526 0.44419Z M0 0.64C0
 0.28654 0.28797 0 0.6432 0H1.4472C1.80243 0 2.0904 0.28654 2.0904
 0.64V7.36C2.0904 7.71346 1.80243 8 1.4472 8H0.6432C0.28797 8 0
 7.71346 0 7.36V0.64ZM3.618 0C3.26277 0 2.9748 0.28654 2.9748
 0.64V7.36C2.9748 7.71346 3.26277 8 3.618 8H4.422C4.77723 8 5.0652
 7.71346 5.0652 7.36V0.64C5.0652 0.28654 4.77723 0 4.422
 0H3.618ZM6.5928 0C6.23757 0 5.9496 0.28654 5.9496 0.64V7.36C5.9496
 7.71346 6.23757 8 6.5928 8H8.04L6.32638 9.7051C6.08514 9.94514 5.9496
 10.2707 5.9496 10.6102V23.36C5.9496 23.7135 6.23757 24 6.5928
 24H7.3968C7.75203 24 8.04 23.7135 8.04 23.36V8V0.64C8.04 0.28654
 7.75203 0 7.3968 0H6.5928ZM0.37678 15.6251C0.13553 15.8651 0 16.1907
 0 16.5302V23.36C0 23.7135 0.28797 24 0.6432 24H1.4472C1.80243 24
 2.0904 23.7135 2.0904 23.36V14.3063C2.0904 14.1637 1.9172 14.0923
 1.81589 14.1931L0.37678 15.6251ZM2.9748 13.5702C2.9748 13.2307
 3.11033 12.9051 3.35158 12.6651L4.7907 11.2331C4.892 11.1323 5.0652
 11.2037 5.0652 11.3463V23.36C5.0652 23.7135 4.77723 24 4.422
 24H3.618C3.26277 24 2.9748 23.7135 2.9748 23.36V13.5702Z" />
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
