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


class HelmIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "helm"

    @property
    def original_file_name(self) -> "str":
        return "helm.svg"

    @property
    def title(self) -> "str":
        return "Helm"

    @property
    def primary_color(self) -> "str":
        return "#0F1689"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Helm</title>
     <path d="M12.337 0c-.475 0-.861 1.016-.861 2.269 0 .527.069
 1.011.183 1.396a8.514 8.514 0 0 0-3.961 1.22 5.229 5.229 0 0
 0-.595-1.093c-.606-.866-1.34-1.436-1.79-1.43a.381.381 0 0
 0-.217.066c-.39.273-.123 1.326.596 2.353.267.381.559.705.84.948a8.683
 8.683 0 0 0-1.528 1.716h1.734a7.179 7.179 0 0 1 5.381-2.421 7.18 7.18
 0 0 1 5.382 2.42h1.733a8.687 8.687 0 0 0-1.32-1.53c.35-.249.735-.643
 1.078-1.133.719-1.027.986-2.08.596-2.353a.382.382 0 0
 0-.217-.065c-.45-.007-1.184.563-1.79 1.43a4.897 4.897 0 0 0-.676
 1.325 8.52 8.52 0 0 0-3.899-1.42c.12-.39.193-.887.193-1.429
 0-1.253-.386-2.269-.862-2.269zM1.624
 9.443v5.162h1.358v-1.968h1.64v1.968h1.357V9.443H4.62v1.838H2.98V9.443zm5.912
 0v5.162h3.21v-1.108H8.893v-.95h1.64v-1.142h-1.64v-.84h1.853V9.443zm4.698
 0v5.162h3.218v-1.362h-1.86v-3.8zm4.706 0v5.162h1.364v-2.643l1.357
 1.225 1.35-1.232v2.65h1.365V9.443h-.614l-2.1
 1.914-2.109-1.914zm-11.82 7.28a8.688 8.688 0 0 0 1.412 1.548 5.206
 5.206 0 0 0-.841.948c-.719 1.027-.985 2.08-.596 2.353.39.273
 1.289-.338 2.007-1.364a5.23 5.23 0 0 0 .595-1.092 8.514 8.514 0 0 0
 3.961 1.219 5.01 5.01 0 0 0-.183 1.396c0 1.253.386 2.269.861
 2.269.476 0 .862-1.016.862-2.269 0-.542-.072-1.04-.193-1.43a8.52 8.52
 0 0 0 3.9-1.42c.121.4.352.865.675 1.327.719 1.026 1.617 1.637 2.007
 1.364.39-.273.123-1.326-.596-2.353-.343-.49-.727-.885-1.077-1.135a8.69
 8.69 0 0 0 1.202-1.36h-1.771a7.174 7.174 0 0 1-5.227 2.252 7.174
 7.174 0 0 1-5.226-2.252z" />
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
