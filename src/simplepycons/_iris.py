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


class IrisIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "iris"

    @property
    def original_file_name(self) -> "str":
        return "iris.svg"

    @property
    def title(self) -> "str":
        return "IRIS"

    @property
    def primary_color(self) -> "str":
        return "#25313C"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>IRIS</title>
     <path d="M21.691
 11.281c-1.26-.322-1.573-.479-1.573-.957v-.021c0-.354.323-.635.937-.635.578
 0 1.174.239
 1.779.639l.074.05c.026.01.055.002.074-.018l.775-1.121a.061.061 0 0
 0-.009-.068c-.023-.015-.044-.034-.068-.05l-.007-.005c-.716-.541-1.584-.843-2.592-.843-1.492
 0-2.552.874-2.552 2.196v.021c0 1.448.949 1.854 2.416 2.228 1.22.313
 1.468.521 1.468.927v.021c0 .427-.396.687-1.052.687-.797
 0-1.461-.315-2.092-.817l-.043-.035a.064.064 0 0 0-.075.012l-.881
 1.049a.069.069 0 0 0 0 .073l.068.059a4.645 4.645 0 0 0 2.986
 1.075c1.572 0 2.676-.813
 2.676-2.259v-.018c.005-1.273-.828-1.805-2.309-2.19ZM5.765
 8.42a.069.069 0 0 1 .068-.065h1.475a.068.068 0 0 1
 .064.068v7.157a.064.064 0 0 1-.064.064H5.829a.068.068 0 0
 1-.067-.064l.003-7.16ZM0
 13.339c0-.035.029-.063.064-.063h1.475a.067.067 0 0 1
 .065.063v2.241a.068.068 0 0 1-.065.064H.064A.064.064 0 0 1 0
 15.58v-2.241ZM15.836 8.42c0-.035.029-.064.064-.064h1.476c.034 0
 .063.029.063.064v7.16a.064.064 0 0 1-.063.064H15.9a.064.064 0 0
 1-.064-.064V8.42Zm-.887 7.172-1.744-2.551c.926-.344 1.559-1.084
 1.559-2.259v-.022c0-.688-.218-1.261-.624-1.667-.478-.477-1.193-.737-2.123-.737H8.749a.064.064
 0 0 0-.063.064v7.16c0 .035.028.064.063.064h1.476a.064.064 0 0 0
 .064-.064v-2.268h1.26l1.559 2.332h1.81c.038 0
 .051-.024.031-.052ZM2.847 10.966a.068.068 0 0 1
 .068-.063h1.47a.068.068 0 0 1 .064.063v4.61a.064.064 0 0
 1-.064.063H2.909a.07.07 0 0
 1-.068-.063l.006-4.61Zm7.448.93.008-2.093h1.578c.782 0 1.26.354 1.26
 1.041v.021c0 .614-.447 1.031-1.228 1.031h-1.618Z" />
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
