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


class NewBalanceIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "newbalance"

    @property
    def original_file_name(self) -> "str":
        return "newbalance.svg"

    @property
    def title(self) -> "str":
        return "New Balance"

    @property
    def primary_color(self) -> "str":
        return "#CF0A2C"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>New Balance</title>
     <path d="M12.169 10.306l1.111-1.937
 3.774-.242.132-.236-3.488-.242.82-1.414h6.47c1.99 0 3.46.715 2.887
 2.8-.17.638-.979 2.233-3.356 2.899.507.06 1.76.616 1.54 2.057-.384
 2.558-3.69 3.774-5.533 3.774l-7.641.006-.38-1.48
 4.005-.28.137-.237-4.346-.264-.467-1.755
 6.178-.363.137-.231-11.096-.693.534-.925
 11.948-.775.138-.231-3.504-.231m5 .385l1.1-.006c.738-.005 1.502-.34
 1.783-1.018.259-.632-.088-1.171-.55-1.166h-1.067l-1.266 2.19zm-1.27
 2.195l-1.326 2.305h1.265c.589 0 1.64-.292
 1.964-1.128.302-.781-.253-1.177-.638-1.177h-1.266zM6.26 16.445l-.77
 1.315L0 17.77l.534-.923 5.726-.402zm.385-10.216l4.417.006.336
 1.248-5.276-.33.523-.924zm5 2.245l.484 1.832-7.542-.495.528-.92
 6.53-.417zm-3.84 5.281l-.957 1.661-5.32-.302.534-.924 5.743-.435z" />
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
