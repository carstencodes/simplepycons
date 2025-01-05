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


class NxpIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "nxp"

    @property
    def original_file_name(self) -> "str":
        return "nxp.svg"

    @property
    def title(self) -> "str":
        return "NXP"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>NXP</title>
     <path d="m6.79652 7.91376 2.52079 4.08625-2.52079
 4.08623-4.27103-4.93862.00088 4.93805-2.52138.00057L0
 16.0792V7.91376h2.52402l4.27103 4.93864.0003-4.93864m14.85075
 2.89478c0-.55173-.27337-.86734-1.0366-.86734h-3.18808v2.31194h3.40456c.59222
 0 .82012-.5576.82012-1.04216v-.40244zm-.62975-2.89478C23.41922
 7.91376 24 9.10757 24 10.70705v.96034c0 1.2164-.53502 2.61319-2.3231
 2.61319h-4.259l.00117 1.80509h-.00117L14.8974
 12l2.52079-4.08625h3.59816m-6.74569.0001h-.4614l-1.70183
 2.71646-1.70184-2.71645H7.4184l2.52109 4.08596-2.52109
 4.08623h2.9872l1.70184-2.71615 1.70183
 2.71615h.4664l2.52019-.00029-2.5205-4.08594 2.5208-4.08596h-2.52549z"
 />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = '''https://www.nxp.com/company/about-nxp/newsroo'''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://www.nxp.com/company/about-nxp/newsroo'''

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
