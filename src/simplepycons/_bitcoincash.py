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


class BitcoinCashIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "bitcoincash"

    @property
    def original_file_name(self) -> "str":
        return "bitcoincash.svg"

    @property
    def title(self) -> "str":
        return "Bitcoin Cash"

    @property
    def primary_color(self) -> "str":
        return "#0AC18E"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Bitcoin Cash</title>
     <path d="m10.84 11.22-.688-2.568c.728-.18 2.839-1.051 3.39.506.27
 1.682-1.978 1.877-2.702 2.062zm.289 1.313.755 2.829c.868-.228
 3.496-.46 3.241-2.351-.433-1.666-3.125-.706-3.996-.478zM24 12c0
 6.627-5.373 12-12 12S0 18.627 0 12 5.373 0 12 0s12 5.373 12
 12zm-6.341.661c-.183-1.151-1.441-2.095-2.485-2.202.643-.57.969-1.401.57-2.488-.603-1.368-1.989-1.66-3.685-1.377l-.546-2.114-1.285.332.536
 2.108c-.338.085-.685.158-1.029.256L9.198 5.08l-1.285.332.545
 2.114c-.277.079-2.595.673-2.595.673l.353
 1.377s.944-.265.935-.244c.524-.137.771.125.886.372l1.498
 5.793c.018.168-.012.454-.372.551.021.012-.935.241-.935.241l.14
 1.605s2.296-.588 2.598-.664l.551 2.138
 1.285-.332-.551-2.153c.353-.082.697-.168 1.032-.256l.548 2.141
 1.285-.332-.551-2.135c1.982-.482 3.38-1.73 3.094-3.64z" />
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
