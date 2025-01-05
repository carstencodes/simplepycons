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


class LaunchpadIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "launchpad"

    @property
    def original_file_name(self) -> "str":
        return "launchpad.svg"

    @property
    def title(self) -> "str":
        return "Launchpad"

    @property
    def primary_color(self) -> "str":
        return "#F8C300"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Launchpad</title>
     <path d="M21.999 18.676l-4.432-2.556-4.783
 2.764V24l9.215-5.324zM11.216 24v-5.119l-4.785-2.762-4.43 2.557L11.216
 24zm.779-6.475l4.789-2.765V9.236l-4.785-2.76-4.783 2.76v5.527l4.781
 2.761-.002.001zM1.22 6.682v10.641l4.432-2.559V9.239L1.219
 6.68l.001.002zm19.615 1.121l-2.484 1.436v5.522l4.43
 2.559V6.678l-1.946 1.125zM2.001 5.324l4.435 2.559
 4.781-2.762V.003L2.001 5.324zm15.566 2.559l4.434-2.559L12.782
 0v5.121l4.785 2.762z" />
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
